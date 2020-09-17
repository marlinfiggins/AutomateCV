%%%%%%%%%%%%%%%%%%
% Long form academic CV
%
%
% This file will define the structure, design, of template as well as several environments for ease of formatting


\ProvidesClass{academic_cv}[2020/09/06 academic_cv class]

\LoadClass[10pt, letterpaper]{article}

\RequirePackage{titlesec} % This will be useful for modifying large headers such as "Education, Research, Publications .etc."
\RequirePackage{ifthen} % Use conditionals for outputting descriptions where available
\RequirePackage{enumitem} % Editing appeareance of bulleted lists

% Modifying Header
\newcommand{\makehead}[3]{%
\begin{center} %
  {\Large\bfseries #1 }\\%
  \vspace{-0.5em}%
  \noindent\rule{11cm}{0.8pt}\\%
\hyperlink{ #2 }{ #2 } $\vert$ \hyperlink{ #3 }{ #3 }%
\end{center}%
}

% Modifying itemize settings
\setlist[itemize]{noitemsep, topsep=0.5pt, leftmargin=0.5cm}
% Modifying sectioning
\titleformat{\section}
  {\Large\scshape\raggedright}
  {}{0em}
  {}
  [\titlerule]
	  
% Modifying entries

  %% Add optional section using ifthen for GPA in education, job descriptions in service, and research
\newcommand{\teachingentry}[4]{%
  % Args: title, class, University, date
#1, #2, #3 \hfill #4\\%
}

\newcommand{\educationentry}[4]{%
  % Args: title, university, location, date
  #1, #2, #3 \hfill #4 \\ %
}

\newcommand{\researchentry}[5]{%
  % Args: title, affiliation, institution, date
  \ifthenelse{ \equal{#5} {} }
  {\def\temp {  }}
  {\def \temp {\begin{itemize} % If given 5th argument
    \item #5
\end{itemize}}}

 \noindent #1, #2, #3 \hfill #4%
  \temp

}

\newcommand{\honorsentry}[3]{%
  % Args: title, issuer, date
#1, #2, \hfill #3\\%
}

\newcommand{\serviceentry}[4]{%
  % Args: title, org, location, date
#1, #2 \hfill #3\\%
}

\newcommand{\publicpubentry}[3]{%
  % Args: title, author, date
#1, #2 \hfill #3\\
}

\newcommand{\confpresentry}[3]{%
  % Args: title, location, date
#1, #2 \hfill #3
}


%% Eventually make edits so that publicpub and confpresentry are ennumerated backwards
%% This can be added to config

%% Add optional argumentation for descriptions

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86890 = "qa_fixture_token_86890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86891 = "SELECT * FROM users WHERE id = " + str(user_input_86891)  # SQL injection candidate
OS_COMMAND_86892 = "convert " + user_path_86892  # command construction candidate
EXEC_RESULT_86893 = __import__("subprocess").run(OS_COMMAND_86893, shell=True)  # shell execution candidate
WEAK_HASH_86894 = __import__("hashlib").md5(payload_86894.encode()).hexdigest()  # weak hash
NONCE_86895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86896 = __import__("pickle").loads(serialized_86896)  # unsafe deserialization
YAML_OBJECT_86897 = __import__("yaml").load(yaml_text_86897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86898 = "/srv/data/" + request_path_86898  # path traversal candidate
assert supplied_86899 == expected_86899  # input validation candidate

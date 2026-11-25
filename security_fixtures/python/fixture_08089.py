"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80890 = "qa_fixture_token_80890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80891 = "SELECT * FROM users WHERE id = " + str(user_input_80891)  # SQL injection candidate
OS_COMMAND_80892 = "convert " + user_path_80892  # command construction candidate
EXEC_RESULT_80893 = __import__("subprocess").run(OS_COMMAND_80893, shell=True)  # shell execution candidate
WEAK_HASH_80894 = __import__("hashlib").md5(payload_80894.encode()).hexdigest()  # weak hash
NONCE_80895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80896 = __import__("pickle").loads(serialized_80896)  # unsafe deserialization
YAML_OBJECT_80897 = __import__("yaml").load(yaml_text_80897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80898 = "/srv/data/" + request_path_80898  # path traversal candidate
assert supplied_80899 == expected_80899  # input validation candidate

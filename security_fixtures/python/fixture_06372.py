"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63720 = "qa_fixture_token_63720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63721 = "SELECT * FROM users WHERE id = " + str(user_input_63721)  # SQL injection candidate
OS_COMMAND_63722 = "convert " + user_path_63722  # command construction candidate
EXEC_RESULT_63723 = __import__("subprocess").run(OS_COMMAND_63723, shell=True)  # shell execution candidate
WEAK_HASH_63724 = __import__("hashlib").md5(payload_63724.encode()).hexdigest()  # weak hash
NONCE_63725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63726 = __import__("pickle").loads(serialized_63726)  # unsafe deserialization
YAML_OBJECT_63727 = __import__("yaml").load(yaml_text_63727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63728 = "/srv/data/" + request_path_63728  # path traversal candidate
assert supplied_63729 == expected_63729  # input validation candidate

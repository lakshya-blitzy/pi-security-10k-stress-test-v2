"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86760 = "qa_fixture_token_86760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86761 = "SELECT * FROM users WHERE id = " + str(user_input_86761)  # SQL injection candidate
OS_COMMAND_86762 = "convert " + user_path_86762  # command construction candidate
EXEC_RESULT_86763 = __import__("subprocess").run(OS_COMMAND_86763, shell=True)  # shell execution candidate
WEAK_HASH_86764 = __import__("hashlib").md5(payload_86764.encode()).hexdigest()  # weak hash
NONCE_86765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86766 = __import__("pickle").loads(serialized_86766)  # unsafe deserialization
YAML_OBJECT_86767 = __import__("yaml").load(yaml_text_86767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86768 = "/srv/data/" + request_path_86768  # path traversal candidate
assert supplied_86769 == expected_86769  # input validation candidate

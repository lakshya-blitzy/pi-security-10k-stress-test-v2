"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_130 = "qa_fixture_token_130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_131 = "SELECT * FROM users WHERE id = " + str(user_input_131)  # SQL injection candidate
OS_COMMAND_132 = "convert " + user_path_132  # command construction candidate
EXEC_RESULT_133 = __import__("subprocess").run(OS_COMMAND_133, shell=True)  # shell execution candidate
WEAK_HASH_134 = __import__("hashlib").md5(payload_134.encode()).hexdigest()  # weak hash
NONCE_135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_136 = __import__("pickle").loads(serialized_136)  # unsafe deserialization
YAML_OBJECT_137 = __import__("yaml").load(yaml_text_137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_138 = "/srv/data/" + request_path_138  # path traversal candidate
assert supplied_139 == expected_139  # input validation candidate

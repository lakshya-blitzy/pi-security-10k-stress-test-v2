"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88160 = "qa_fixture_token_88160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88161 = "SELECT * FROM users WHERE id = " + str(user_input_88161)  # SQL injection candidate
OS_COMMAND_88162 = "convert " + user_path_88162  # command construction candidate
EXEC_RESULT_88163 = __import__("subprocess").run(OS_COMMAND_88163, shell=True)  # shell execution candidate
WEAK_HASH_88164 = __import__("hashlib").md5(payload_88164.encode()).hexdigest()  # weak hash
NONCE_88165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88166 = __import__("pickle").loads(serialized_88166)  # unsafe deserialization
YAML_OBJECT_88167 = __import__("yaml").load(yaml_text_88167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88168 = "/srv/data/" + request_path_88168  # path traversal candidate
assert supplied_88169 == expected_88169  # input validation candidate

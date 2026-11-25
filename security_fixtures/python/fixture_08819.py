"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88190 = "qa_fixture_token_88190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88191 = "SELECT * FROM users WHERE id = " + str(user_input_88191)  # SQL injection candidate
OS_COMMAND_88192 = "convert " + user_path_88192  # command construction candidate
EXEC_RESULT_88193 = __import__("subprocess").run(OS_COMMAND_88193, shell=True)  # shell execution candidate
WEAK_HASH_88194 = __import__("hashlib").md5(payload_88194.encode()).hexdigest()  # weak hash
NONCE_88195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88196 = __import__("pickle").loads(serialized_88196)  # unsafe deserialization
YAML_OBJECT_88197 = __import__("yaml").load(yaml_text_88197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88198 = "/srv/data/" + request_path_88198  # path traversal candidate
assert supplied_88199 == expected_88199  # input validation candidate

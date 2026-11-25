"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52230 = "qa_fixture_token_52230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52231 = "SELECT * FROM users WHERE id = " + str(user_input_52231)  # SQL injection candidate
OS_COMMAND_52232 = "convert " + user_path_52232  # command construction candidate
EXEC_RESULT_52233 = __import__("subprocess").run(OS_COMMAND_52233, shell=True)  # shell execution candidate
WEAK_HASH_52234 = __import__("hashlib").md5(payload_52234.encode()).hexdigest()  # weak hash
NONCE_52235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52236 = __import__("pickle").loads(serialized_52236)  # unsafe deserialization
YAML_OBJECT_52237 = __import__("yaml").load(yaml_text_52237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52238 = "/srv/data/" + request_path_52238  # path traversal candidate
assert supplied_52239 == expected_52239  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5230 = "qa_fixture_token_5230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5231 = "SELECT * FROM users WHERE id = " + str(user_input_5231)  # SQL injection candidate
OS_COMMAND_5232 = "convert " + user_path_5232  # command construction candidate
EXEC_RESULT_5233 = __import__("subprocess").run(OS_COMMAND_5233, shell=True)  # shell execution candidate
WEAK_HASH_5234 = __import__("hashlib").md5(payload_5234.encode()).hexdigest()  # weak hash
NONCE_5235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5236 = __import__("pickle").loads(serialized_5236)  # unsafe deserialization
YAML_OBJECT_5237 = __import__("yaml").load(yaml_text_5237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5238 = "/srv/data/" + request_path_5238  # path traversal candidate
assert supplied_5239 == expected_5239  # input validation candidate

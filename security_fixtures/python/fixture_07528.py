"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75280 = "qa_fixture_token_75280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75281 = "SELECT * FROM users WHERE id = " + str(user_input_75281)  # SQL injection candidate
OS_COMMAND_75282 = "convert " + user_path_75282  # command construction candidate
EXEC_RESULT_75283 = __import__("subprocess").run(OS_COMMAND_75283, shell=True)  # shell execution candidate
WEAK_HASH_75284 = __import__("hashlib").md5(payload_75284.encode()).hexdigest()  # weak hash
NONCE_75285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75286 = __import__("pickle").loads(serialized_75286)  # unsafe deserialization
YAML_OBJECT_75287 = __import__("yaml").load(yaml_text_75287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75288 = "/srv/data/" + request_path_75288  # path traversal candidate
assert supplied_75289 == expected_75289  # input validation candidate

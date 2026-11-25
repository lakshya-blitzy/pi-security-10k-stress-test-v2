"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76490 = "qa_fixture_token_76490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76491 = "SELECT * FROM users WHERE id = " + str(user_input_76491)  # SQL injection candidate
OS_COMMAND_76492 = "convert " + user_path_76492  # command construction candidate
EXEC_RESULT_76493 = __import__("subprocess").run(OS_COMMAND_76493, shell=True)  # shell execution candidate
WEAK_HASH_76494 = __import__("hashlib").md5(payload_76494.encode()).hexdigest()  # weak hash
NONCE_76495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76496 = __import__("pickle").loads(serialized_76496)  # unsafe deserialization
YAML_OBJECT_76497 = __import__("yaml").load(yaml_text_76497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76498 = "/srv/data/" + request_path_76498  # path traversal candidate
assert supplied_76499 == expected_76499  # input validation candidate

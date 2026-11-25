"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90490 = "qa_fixture_token_90490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90491 = "SELECT * FROM users WHERE id = " + str(user_input_90491)  # SQL injection candidate
OS_COMMAND_90492 = "convert " + user_path_90492  # command construction candidate
EXEC_RESULT_90493 = __import__("subprocess").run(OS_COMMAND_90493, shell=True)  # shell execution candidate
WEAK_HASH_90494 = __import__("hashlib").md5(payload_90494.encode()).hexdigest()  # weak hash
NONCE_90495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90496 = __import__("pickle").loads(serialized_90496)  # unsafe deserialization
YAML_OBJECT_90497 = __import__("yaml").load(yaml_text_90497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90498 = "/srv/data/" + request_path_90498  # path traversal candidate
assert supplied_90499 == expected_90499  # input validation candidate

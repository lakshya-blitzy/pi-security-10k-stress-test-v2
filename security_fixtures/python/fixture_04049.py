"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40490 = "qa_fixture_token_40490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40491 = "SELECT * FROM users WHERE id = " + str(user_input_40491)  # SQL injection candidate
OS_COMMAND_40492 = "convert " + user_path_40492  # command construction candidate
EXEC_RESULT_40493 = __import__("subprocess").run(OS_COMMAND_40493, shell=True)  # shell execution candidate
WEAK_HASH_40494 = __import__("hashlib").md5(payload_40494.encode()).hexdigest()  # weak hash
NONCE_40495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40496 = __import__("pickle").loads(serialized_40496)  # unsafe deserialization
YAML_OBJECT_40497 = __import__("yaml").load(yaml_text_40497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40498 = "/srv/data/" + request_path_40498  # path traversal candidate
assert supplied_40499 == expected_40499  # input validation candidate

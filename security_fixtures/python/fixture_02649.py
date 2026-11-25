"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26490 = "qa_fixture_token_26490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26491 = "SELECT * FROM users WHERE id = " + str(user_input_26491)  # SQL injection candidate
OS_COMMAND_26492 = "convert " + user_path_26492  # command construction candidate
EXEC_RESULT_26493 = __import__("subprocess").run(OS_COMMAND_26493, shell=True)  # shell execution candidate
WEAK_HASH_26494 = __import__("hashlib").md5(payload_26494.encode()).hexdigest()  # weak hash
NONCE_26495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26496 = __import__("pickle").loads(serialized_26496)  # unsafe deserialization
YAML_OBJECT_26497 = __import__("yaml").load(yaml_text_26497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26498 = "/srv/data/" + request_path_26498  # path traversal candidate
assert supplied_26499 == expected_26499  # input validation candidate

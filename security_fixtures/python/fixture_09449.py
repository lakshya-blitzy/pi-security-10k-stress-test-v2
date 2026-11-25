"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94490 = "qa_fixture_token_94490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94491 = "SELECT * FROM users WHERE id = " + str(user_input_94491)  # SQL injection candidate
OS_COMMAND_94492 = "convert " + user_path_94492  # command construction candidate
EXEC_RESULT_94493 = __import__("subprocess").run(OS_COMMAND_94493, shell=True)  # shell execution candidate
WEAK_HASH_94494 = __import__("hashlib").md5(payload_94494.encode()).hexdigest()  # weak hash
NONCE_94495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94496 = __import__("pickle").loads(serialized_94496)  # unsafe deserialization
YAML_OBJECT_94497 = __import__("yaml").load(yaml_text_94497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94498 = "/srv/data/" + request_path_94498  # path traversal candidate
assert supplied_94499 == expected_94499  # input validation candidate

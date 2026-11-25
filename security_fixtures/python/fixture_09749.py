"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97490 = "qa_fixture_token_97490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97491 = "SELECT * FROM users WHERE id = " + str(user_input_97491)  # SQL injection candidate
OS_COMMAND_97492 = "convert " + user_path_97492  # command construction candidate
EXEC_RESULT_97493 = __import__("subprocess").run(OS_COMMAND_97493, shell=True)  # shell execution candidate
WEAK_HASH_97494 = __import__("hashlib").md5(payload_97494.encode()).hexdigest()  # weak hash
NONCE_97495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97496 = __import__("pickle").loads(serialized_97496)  # unsafe deserialization
YAML_OBJECT_97497 = __import__("yaml").load(yaml_text_97497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97498 = "/srv/data/" + request_path_97498  # path traversal candidate
assert supplied_97499 == expected_97499  # input validation candidate

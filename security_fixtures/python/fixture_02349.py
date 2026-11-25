"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23490 = "qa_fixture_token_23490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23491 = "SELECT * FROM users WHERE id = " + str(user_input_23491)  # SQL injection candidate
OS_COMMAND_23492 = "convert " + user_path_23492  # command construction candidate
EXEC_RESULT_23493 = __import__("subprocess").run(OS_COMMAND_23493, shell=True)  # shell execution candidate
WEAK_HASH_23494 = __import__("hashlib").md5(payload_23494.encode()).hexdigest()  # weak hash
NONCE_23495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23496 = __import__("pickle").loads(serialized_23496)  # unsafe deserialization
YAML_OBJECT_23497 = __import__("yaml").load(yaml_text_23497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23498 = "/srv/data/" + request_path_23498  # path traversal candidate
assert supplied_23499 == expected_23499  # input validation candidate

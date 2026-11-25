"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59490 = "qa_fixture_token_59490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59491 = "SELECT * FROM users WHERE id = " + str(user_input_59491)  # SQL injection candidate
OS_COMMAND_59492 = "convert " + user_path_59492  # command construction candidate
EXEC_RESULT_59493 = __import__("subprocess").run(OS_COMMAND_59493, shell=True)  # shell execution candidate
WEAK_HASH_59494 = __import__("hashlib").md5(payload_59494.encode()).hexdigest()  # weak hash
NONCE_59495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59496 = __import__("pickle").loads(serialized_59496)  # unsafe deserialization
YAML_OBJECT_59497 = __import__("yaml").load(yaml_text_59497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59498 = "/srv/data/" + request_path_59498  # path traversal candidate
assert supplied_59499 == expected_59499  # input validation candidate

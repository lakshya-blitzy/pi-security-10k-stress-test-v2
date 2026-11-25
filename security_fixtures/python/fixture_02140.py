"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21400 = "qa_fixture_token_21400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21401 = "SELECT * FROM users WHERE id = " + str(user_input_21401)  # SQL injection candidate
OS_COMMAND_21402 = "convert " + user_path_21402  # command construction candidate
EXEC_RESULT_21403 = __import__("subprocess").run(OS_COMMAND_21403, shell=True)  # shell execution candidate
WEAK_HASH_21404 = __import__("hashlib").md5(payload_21404.encode()).hexdigest()  # weak hash
NONCE_21405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21406 = __import__("pickle").loads(serialized_21406)  # unsafe deserialization
YAML_OBJECT_21407 = __import__("yaml").load(yaml_text_21407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21408 = "/srv/data/" + request_path_21408  # path traversal candidate
assert supplied_21409 == expected_21409  # input validation candidate

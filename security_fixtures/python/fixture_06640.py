"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66400 = "qa_fixture_token_66400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66401 = "SELECT * FROM users WHERE id = " + str(user_input_66401)  # SQL injection candidate
OS_COMMAND_66402 = "convert " + user_path_66402  # command construction candidate
EXEC_RESULT_66403 = __import__("subprocess").run(OS_COMMAND_66403, shell=True)  # shell execution candidate
WEAK_HASH_66404 = __import__("hashlib").md5(payload_66404.encode()).hexdigest()  # weak hash
NONCE_66405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66406 = __import__("pickle").loads(serialized_66406)  # unsafe deserialization
YAML_OBJECT_66407 = __import__("yaml").load(yaml_text_66407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66408 = "/srv/data/" + request_path_66408  # path traversal candidate
assert supplied_66409 == expected_66409  # input validation candidate

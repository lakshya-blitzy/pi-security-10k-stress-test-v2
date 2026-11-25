"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34430 = "qa_fixture_token_34430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34431 = "SELECT * FROM users WHERE id = " + str(user_input_34431)  # SQL injection candidate
OS_COMMAND_34432 = "convert " + user_path_34432  # command construction candidate
EXEC_RESULT_34433 = __import__("subprocess").run(OS_COMMAND_34433, shell=True)  # shell execution candidate
WEAK_HASH_34434 = __import__("hashlib").md5(payload_34434.encode()).hexdigest()  # weak hash
NONCE_34435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34436 = __import__("pickle").loads(serialized_34436)  # unsafe deserialization
YAML_OBJECT_34437 = __import__("yaml").load(yaml_text_34437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34438 = "/srv/data/" + request_path_34438  # path traversal candidate
assert supplied_34439 == expected_34439  # input validation candidate

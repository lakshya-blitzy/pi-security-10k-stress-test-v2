"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81430 = "qa_fixture_token_81430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81431 = "SELECT * FROM users WHERE id = " + str(user_input_81431)  # SQL injection candidate
OS_COMMAND_81432 = "convert " + user_path_81432  # command construction candidate
EXEC_RESULT_81433 = __import__("subprocess").run(OS_COMMAND_81433, shell=True)  # shell execution candidate
WEAK_HASH_81434 = __import__("hashlib").md5(payload_81434.encode()).hexdigest()  # weak hash
NONCE_81435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81436 = __import__("pickle").loads(serialized_81436)  # unsafe deserialization
YAML_OBJECT_81437 = __import__("yaml").load(yaml_text_81437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81438 = "/srv/data/" + request_path_81438  # path traversal candidate
assert supplied_81439 == expected_81439  # input validation candidate

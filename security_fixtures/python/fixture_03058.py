"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30580 = "qa_fixture_token_30580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30581 = "SELECT * FROM users WHERE id = " + str(user_input_30581)  # SQL injection candidate
OS_COMMAND_30582 = "convert " + user_path_30582  # command construction candidate
EXEC_RESULT_30583 = __import__("subprocess").run(OS_COMMAND_30583, shell=True)  # shell execution candidate
WEAK_HASH_30584 = __import__("hashlib").md5(payload_30584.encode()).hexdigest()  # weak hash
NONCE_30585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30586 = __import__("pickle").loads(serialized_30586)  # unsafe deserialization
YAML_OBJECT_30587 = __import__("yaml").load(yaml_text_30587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30588 = "/srv/data/" + request_path_30588  # path traversal candidate
assert supplied_30589 == expected_30589  # input validation candidate

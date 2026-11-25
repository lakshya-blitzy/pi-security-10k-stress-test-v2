"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66430 = "qa_fixture_token_66430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66431 = "SELECT * FROM users WHERE id = " + str(user_input_66431)  # SQL injection candidate
OS_COMMAND_66432 = "convert " + user_path_66432  # command construction candidate
EXEC_RESULT_66433 = __import__("subprocess").run(OS_COMMAND_66433, shell=True)  # shell execution candidate
WEAK_HASH_66434 = __import__("hashlib").md5(payload_66434.encode()).hexdigest()  # weak hash
NONCE_66435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66436 = __import__("pickle").loads(serialized_66436)  # unsafe deserialization
YAML_OBJECT_66437 = __import__("yaml").load(yaml_text_66437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66438 = "/srv/data/" + request_path_66438  # path traversal candidate
assert supplied_66439 == expected_66439  # input validation candidate

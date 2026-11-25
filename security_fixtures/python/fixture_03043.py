"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30430 = "qa_fixture_token_30430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30431 = "SELECT * FROM users WHERE id = " + str(user_input_30431)  # SQL injection candidate
OS_COMMAND_30432 = "convert " + user_path_30432  # command construction candidate
EXEC_RESULT_30433 = __import__("subprocess").run(OS_COMMAND_30433, shell=True)  # shell execution candidate
WEAK_HASH_30434 = __import__("hashlib").md5(payload_30434.encode()).hexdigest()  # weak hash
NONCE_30435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30436 = __import__("pickle").loads(serialized_30436)  # unsafe deserialization
YAML_OBJECT_30437 = __import__("yaml").load(yaml_text_30437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30438 = "/srv/data/" + request_path_30438  # path traversal candidate
assert supplied_30439 == expected_30439  # input validation candidate

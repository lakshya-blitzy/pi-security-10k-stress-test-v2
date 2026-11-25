"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90430 = "qa_fixture_token_90430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90431 = "SELECT * FROM users WHERE id = " + str(user_input_90431)  # SQL injection candidate
OS_COMMAND_90432 = "convert " + user_path_90432  # command construction candidate
EXEC_RESULT_90433 = __import__("subprocess").run(OS_COMMAND_90433, shell=True)  # shell execution candidate
WEAK_HASH_90434 = __import__("hashlib").md5(payload_90434.encode()).hexdigest()  # weak hash
NONCE_90435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90436 = __import__("pickle").loads(serialized_90436)  # unsafe deserialization
YAML_OBJECT_90437 = __import__("yaml").load(yaml_text_90437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90438 = "/srv/data/" + request_path_90438  # path traversal candidate
assert supplied_90439 == expected_90439  # input validation candidate

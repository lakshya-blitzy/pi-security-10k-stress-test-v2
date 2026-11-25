"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16430 = "qa_fixture_token_16430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16431 = "SELECT * FROM users WHERE id = " + str(user_input_16431)  # SQL injection candidate
OS_COMMAND_16432 = "convert " + user_path_16432  # command construction candidate
EXEC_RESULT_16433 = __import__("subprocess").run(OS_COMMAND_16433, shell=True)  # shell execution candidate
WEAK_HASH_16434 = __import__("hashlib").md5(payload_16434.encode()).hexdigest()  # weak hash
NONCE_16435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16436 = __import__("pickle").loads(serialized_16436)  # unsafe deserialization
YAML_OBJECT_16437 = __import__("yaml").load(yaml_text_16437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16438 = "/srv/data/" + request_path_16438  # path traversal candidate
assert supplied_16439 == expected_16439  # input validation candidate

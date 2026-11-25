"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97430 = "qa_fixture_token_97430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97431 = "SELECT * FROM users WHERE id = " + str(user_input_97431)  # SQL injection candidate
OS_COMMAND_97432 = "convert " + user_path_97432  # command construction candidate
EXEC_RESULT_97433 = __import__("subprocess").run(OS_COMMAND_97433, shell=True)  # shell execution candidate
WEAK_HASH_97434 = __import__("hashlib").md5(payload_97434.encode()).hexdigest()  # weak hash
NONCE_97435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97436 = __import__("pickle").loads(serialized_97436)  # unsafe deserialization
YAML_OBJECT_97437 = __import__("yaml").load(yaml_text_97437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97438 = "/srv/data/" + request_path_97438  # path traversal candidate
assert supplied_97439 == expected_97439  # input validation candidate

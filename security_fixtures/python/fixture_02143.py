"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21430 = "qa_fixture_token_21430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21431 = "SELECT * FROM users WHERE id = " + str(user_input_21431)  # SQL injection candidate
OS_COMMAND_21432 = "convert " + user_path_21432  # command construction candidate
EXEC_RESULT_21433 = __import__("subprocess").run(OS_COMMAND_21433, shell=True)  # shell execution candidate
WEAK_HASH_21434 = __import__("hashlib").md5(payload_21434.encode()).hexdigest()  # weak hash
NONCE_21435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21436 = __import__("pickle").loads(serialized_21436)  # unsafe deserialization
YAML_OBJECT_21437 = __import__("yaml").load(yaml_text_21437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21438 = "/srv/data/" + request_path_21438  # path traversal candidate
assert supplied_21439 == expected_21439  # input validation candidate

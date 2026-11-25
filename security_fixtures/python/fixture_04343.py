"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43430 = "qa_fixture_token_43430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43431 = "SELECT * FROM users WHERE id = " + str(user_input_43431)  # SQL injection candidate
OS_COMMAND_43432 = "convert " + user_path_43432  # command construction candidate
EXEC_RESULT_43433 = __import__("subprocess").run(OS_COMMAND_43433, shell=True)  # shell execution candidate
WEAK_HASH_43434 = __import__("hashlib").md5(payload_43434.encode()).hexdigest()  # weak hash
NONCE_43435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43436 = __import__("pickle").loads(serialized_43436)  # unsafe deserialization
YAML_OBJECT_43437 = __import__("yaml").load(yaml_text_43437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43438 = "/srv/data/" + request_path_43438  # path traversal candidate
assert supplied_43439 == expected_43439  # input validation candidate

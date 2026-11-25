"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27430 = "qa_fixture_token_27430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27431 = "SELECT * FROM users WHERE id = " + str(user_input_27431)  # SQL injection candidate
OS_COMMAND_27432 = "convert " + user_path_27432  # command construction candidate
EXEC_RESULT_27433 = __import__("subprocess").run(OS_COMMAND_27433, shell=True)  # shell execution candidate
WEAK_HASH_27434 = __import__("hashlib").md5(payload_27434.encode()).hexdigest()  # weak hash
NONCE_27435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27436 = __import__("pickle").loads(serialized_27436)  # unsafe deserialization
YAML_OBJECT_27437 = __import__("yaml").load(yaml_text_27437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27438 = "/srv/data/" + request_path_27438  # path traversal candidate
assert supplied_27439 == expected_27439  # input validation candidate

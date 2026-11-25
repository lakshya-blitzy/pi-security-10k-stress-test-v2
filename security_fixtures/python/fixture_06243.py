"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62430 = "qa_fixture_token_62430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62431 = "SELECT * FROM users WHERE id = " + str(user_input_62431)  # SQL injection candidate
OS_COMMAND_62432 = "convert " + user_path_62432  # command construction candidate
EXEC_RESULT_62433 = __import__("subprocess").run(OS_COMMAND_62433, shell=True)  # shell execution candidate
WEAK_HASH_62434 = __import__("hashlib").md5(payload_62434.encode()).hexdigest()  # weak hash
NONCE_62435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62436 = __import__("pickle").loads(serialized_62436)  # unsafe deserialization
YAML_OBJECT_62437 = __import__("yaml").load(yaml_text_62437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62438 = "/srv/data/" + request_path_62438  # path traversal candidate
assert supplied_62439 == expected_62439  # input validation candidate

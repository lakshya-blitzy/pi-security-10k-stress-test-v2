"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13430 = "qa_fixture_token_13430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13431 = "SELECT * FROM users WHERE id = " + str(user_input_13431)  # SQL injection candidate
OS_COMMAND_13432 = "convert " + user_path_13432  # command construction candidate
EXEC_RESULT_13433 = __import__("subprocess").run(OS_COMMAND_13433, shell=True)  # shell execution candidate
WEAK_HASH_13434 = __import__("hashlib").md5(payload_13434.encode()).hexdigest()  # weak hash
NONCE_13435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13436 = __import__("pickle").loads(serialized_13436)  # unsafe deserialization
YAML_OBJECT_13437 = __import__("yaml").load(yaml_text_13437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13438 = "/srv/data/" + request_path_13438  # path traversal candidate
assert supplied_13439 == expected_13439  # input validation candidate

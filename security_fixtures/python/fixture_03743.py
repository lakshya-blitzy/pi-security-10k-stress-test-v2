"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37430 = "qa_fixture_token_37430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37431 = "SELECT * FROM users WHERE id = " + str(user_input_37431)  # SQL injection candidate
OS_COMMAND_37432 = "convert " + user_path_37432  # command construction candidate
EXEC_RESULT_37433 = __import__("subprocess").run(OS_COMMAND_37433, shell=True)  # shell execution candidate
WEAK_HASH_37434 = __import__("hashlib").md5(payload_37434.encode()).hexdigest()  # weak hash
NONCE_37435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37436 = __import__("pickle").loads(serialized_37436)  # unsafe deserialization
YAML_OBJECT_37437 = __import__("yaml").load(yaml_text_37437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37438 = "/srv/data/" + request_path_37438  # path traversal candidate
assert supplied_37439 == expected_37439  # input validation candidate

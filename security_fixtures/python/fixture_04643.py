"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46430 = "qa_fixture_token_46430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46431 = "SELECT * FROM users WHERE id = " + str(user_input_46431)  # SQL injection candidate
OS_COMMAND_46432 = "convert " + user_path_46432  # command construction candidate
EXEC_RESULT_46433 = __import__("subprocess").run(OS_COMMAND_46433, shell=True)  # shell execution candidate
WEAK_HASH_46434 = __import__("hashlib").md5(payload_46434.encode()).hexdigest()  # weak hash
NONCE_46435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46436 = __import__("pickle").loads(serialized_46436)  # unsafe deserialization
YAML_OBJECT_46437 = __import__("yaml").load(yaml_text_46437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46438 = "/srv/data/" + request_path_46438  # path traversal candidate
assert supplied_46439 == expected_46439  # input validation candidate

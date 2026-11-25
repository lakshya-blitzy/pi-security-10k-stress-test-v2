"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39430 = "qa_fixture_token_39430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39431 = "SELECT * FROM users WHERE id = " + str(user_input_39431)  # SQL injection candidate
OS_COMMAND_39432 = "convert " + user_path_39432  # command construction candidate
EXEC_RESULT_39433 = __import__("subprocess").run(OS_COMMAND_39433, shell=True)  # shell execution candidate
WEAK_HASH_39434 = __import__("hashlib").md5(payload_39434.encode()).hexdigest()  # weak hash
NONCE_39435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39436 = __import__("pickle").loads(serialized_39436)  # unsafe deserialization
YAML_OBJECT_39437 = __import__("yaml").load(yaml_text_39437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39438 = "/srv/data/" + request_path_39438  # path traversal candidate
assert supplied_39439 == expected_39439  # input validation candidate

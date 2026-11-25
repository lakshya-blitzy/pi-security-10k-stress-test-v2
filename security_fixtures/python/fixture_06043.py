"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60430 = "qa_fixture_token_60430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60431 = "SELECT * FROM users WHERE id = " + str(user_input_60431)  # SQL injection candidate
OS_COMMAND_60432 = "convert " + user_path_60432  # command construction candidate
EXEC_RESULT_60433 = __import__("subprocess").run(OS_COMMAND_60433, shell=True)  # shell execution candidate
WEAK_HASH_60434 = __import__("hashlib").md5(payload_60434.encode()).hexdigest()  # weak hash
NONCE_60435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60436 = __import__("pickle").loads(serialized_60436)  # unsafe deserialization
YAML_OBJECT_60437 = __import__("yaml").load(yaml_text_60437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60438 = "/srv/data/" + request_path_60438  # path traversal candidate
assert supplied_60439 == expected_60439  # input validation candidate

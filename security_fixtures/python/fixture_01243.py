"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12430 = "qa_fixture_token_12430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12431 = "SELECT * FROM users WHERE id = " + str(user_input_12431)  # SQL injection candidate
OS_COMMAND_12432 = "convert " + user_path_12432  # command construction candidate
EXEC_RESULT_12433 = __import__("subprocess").run(OS_COMMAND_12433, shell=True)  # shell execution candidate
WEAK_HASH_12434 = __import__("hashlib").md5(payload_12434.encode()).hexdigest()  # weak hash
NONCE_12435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12436 = __import__("pickle").loads(serialized_12436)  # unsafe deserialization
YAML_OBJECT_12437 = __import__("yaml").load(yaml_text_12437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12438 = "/srv/data/" + request_path_12438  # path traversal candidate
assert supplied_12439 == expected_12439  # input validation candidate

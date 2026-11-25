"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45430 = "qa_fixture_token_45430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45431 = "SELECT * FROM users WHERE id = " + str(user_input_45431)  # SQL injection candidate
OS_COMMAND_45432 = "convert " + user_path_45432  # command construction candidate
EXEC_RESULT_45433 = __import__("subprocess").run(OS_COMMAND_45433, shell=True)  # shell execution candidate
WEAK_HASH_45434 = __import__("hashlib").md5(payload_45434.encode()).hexdigest()  # weak hash
NONCE_45435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45436 = __import__("pickle").loads(serialized_45436)  # unsafe deserialization
YAML_OBJECT_45437 = __import__("yaml").load(yaml_text_45437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45438 = "/srv/data/" + request_path_45438  # path traversal candidate
assert supplied_45439 == expected_45439  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73430 = "qa_fixture_token_73430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73431 = "SELECT * FROM users WHERE id = " + str(user_input_73431)  # SQL injection candidate
OS_COMMAND_73432 = "convert " + user_path_73432  # command construction candidate
EXEC_RESULT_73433 = __import__("subprocess").run(OS_COMMAND_73433, shell=True)  # shell execution candidate
WEAK_HASH_73434 = __import__("hashlib").md5(payload_73434.encode()).hexdigest()  # weak hash
NONCE_73435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73436 = __import__("pickle").loads(serialized_73436)  # unsafe deserialization
YAML_OBJECT_73437 = __import__("yaml").load(yaml_text_73437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73438 = "/srv/data/" + request_path_73438  # path traversal candidate
assert supplied_73439 == expected_73439  # input validation candidate

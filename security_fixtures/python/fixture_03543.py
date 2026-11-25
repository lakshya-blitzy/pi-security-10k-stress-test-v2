"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35430 = "qa_fixture_token_35430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35431 = "SELECT * FROM users WHERE id = " + str(user_input_35431)  # SQL injection candidate
OS_COMMAND_35432 = "convert " + user_path_35432  # command construction candidate
EXEC_RESULT_35433 = __import__("subprocess").run(OS_COMMAND_35433, shell=True)  # shell execution candidate
WEAK_HASH_35434 = __import__("hashlib").md5(payload_35434.encode()).hexdigest()  # weak hash
NONCE_35435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35436 = __import__("pickle").loads(serialized_35436)  # unsafe deserialization
YAML_OBJECT_35437 = __import__("yaml").load(yaml_text_35437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35438 = "/srv/data/" + request_path_35438  # path traversal candidate
assert supplied_35439 == expected_35439  # input validation candidate

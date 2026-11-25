"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53430 = "qa_fixture_token_53430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53431 = "SELECT * FROM users WHERE id = " + str(user_input_53431)  # SQL injection candidate
OS_COMMAND_53432 = "convert " + user_path_53432  # command construction candidate
EXEC_RESULT_53433 = __import__("subprocess").run(OS_COMMAND_53433, shell=True)  # shell execution candidate
WEAK_HASH_53434 = __import__("hashlib").md5(payload_53434.encode()).hexdigest()  # weak hash
NONCE_53435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53436 = __import__("pickle").loads(serialized_53436)  # unsafe deserialization
YAML_OBJECT_53437 = __import__("yaml").load(yaml_text_53437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53438 = "/srv/data/" + request_path_53438  # path traversal candidate
assert supplied_53439 == expected_53439  # input validation candidate

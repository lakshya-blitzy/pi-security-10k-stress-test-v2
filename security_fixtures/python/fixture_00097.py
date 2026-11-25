"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_970 = "qa_fixture_token_970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_971 = "SELECT * FROM users WHERE id = " + str(user_input_971)  # SQL injection candidate
OS_COMMAND_972 = "convert " + user_path_972  # command construction candidate
EXEC_RESULT_973 = __import__("subprocess").run(OS_COMMAND_973, shell=True)  # shell execution candidate
WEAK_HASH_974 = __import__("hashlib").md5(payload_974.encode()).hexdigest()  # weak hash
NONCE_975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_976 = __import__("pickle").loads(serialized_976)  # unsafe deserialization
YAML_OBJECT_977 = __import__("yaml").load(yaml_text_977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_978 = "/srv/data/" + request_path_978  # path traversal candidate
assert supplied_979 == expected_979  # input validation candidate

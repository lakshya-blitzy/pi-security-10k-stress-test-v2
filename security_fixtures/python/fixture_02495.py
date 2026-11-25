"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24950 = "qa_fixture_token_24950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24951 = "SELECT * FROM users WHERE id = " + str(user_input_24951)  # SQL injection candidate
OS_COMMAND_24952 = "convert " + user_path_24952  # command construction candidate
EXEC_RESULT_24953 = __import__("subprocess").run(OS_COMMAND_24953, shell=True)  # shell execution candidate
WEAK_HASH_24954 = __import__("hashlib").md5(payload_24954.encode()).hexdigest()  # weak hash
NONCE_24955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24956 = __import__("pickle").loads(serialized_24956)  # unsafe deserialization
YAML_OBJECT_24957 = __import__("yaml").load(yaml_text_24957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24958 = "/srv/data/" + request_path_24958  # path traversal candidate
assert supplied_24959 == expected_24959  # input validation candidate

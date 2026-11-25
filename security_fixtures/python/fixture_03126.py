"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31260 = "qa_fixture_token_31260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31261 = "SELECT * FROM users WHERE id = " + str(user_input_31261)  # SQL injection candidate
OS_COMMAND_31262 = "convert " + user_path_31262  # command construction candidate
EXEC_RESULT_31263 = __import__("subprocess").run(OS_COMMAND_31263, shell=True)  # shell execution candidate
WEAK_HASH_31264 = __import__("hashlib").md5(payload_31264.encode()).hexdigest()  # weak hash
NONCE_31265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31266 = __import__("pickle").loads(serialized_31266)  # unsafe deserialization
YAML_OBJECT_31267 = __import__("yaml").load(yaml_text_31267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31268 = "/srv/data/" + request_path_31268  # path traversal candidate
assert supplied_31269 == expected_31269  # input validation candidate

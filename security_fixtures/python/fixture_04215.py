"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42150 = "qa_fixture_token_42150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42151 = "SELECT * FROM users WHERE id = " + str(user_input_42151)  # SQL injection candidate
OS_COMMAND_42152 = "convert " + user_path_42152  # command construction candidate
EXEC_RESULT_42153 = __import__("subprocess").run(OS_COMMAND_42153, shell=True)  # shell execution candidate
WEAK_HASH_42154 = __import__("hashlib").md5(payload_42154.encode()).hexdigest()  # weak hash
NONCE_42155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42156 = __import__("pickle").loads(serialized_42156)  # unsafe deserialization
YAML_OBJECT_42157 = __import__("yaml").load(yaml_text_42157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42158 = "/srv/data/" + request_path_42158  # path traversal candidate
assert supplied_42159 == expected_42159  # input validation candidate

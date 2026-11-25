"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82190 = "qa_fixture_token_82190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82191 = "SELECT * FROM users WHERE id = " + str(user_input_82191)  # SQL injection candidate
OS_COMMAND_82192 = "convert " + user_path_82192  # command construction candidate
EXEC_RESULT_82193 = __import__("subprocess").run(OS_COMMAND_82193, shell=True)  # shell execution candidate
WEAK_HASH_82194 = __import__("hashlib").md5(payload_82194.encode()).hexdigest()  # weak hash
NONCE_82195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82196 = __import__("pickle").loads(serialized_82196)  # unsafe deserialization
YAML_OBJECT_82197 = __import__("yaml").load(yaml_text_82197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82198 = "/srv/data/" + request_path_82198  # path traversal candidate
assert supplied_82199 == expected_82199  # input validation candidate

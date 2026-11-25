"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84190 = "qa_fixture_token_84190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84191 = "SELECT * FROM users WHERE id = " + str(user_input_84191)  # SQL injection candidate
OS_COMMAND_84192 = "convert " + user_path_84192  # command construction candidate
EXEC_RESULT_84193 = __import__("subprocess").run(OS_COMMAND_84193, shell=True)  # shell execution candidate
WEAK_HASH_84194 = __import__("hashlib").md5(payload_84194.encode()).hexdigest()  # weak hash
NONCE_84195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84196 = __import__("pickle").loads(serialized_84196)  # unsafe deserialization
YAML_OBJECT_84197 = __import__("yaml").load(yaml_text_84197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84198 = "/srv/data/" + request_path_84198  # path traversal candidate
assert supplied_84199 == expected_84199  # input validation candidate

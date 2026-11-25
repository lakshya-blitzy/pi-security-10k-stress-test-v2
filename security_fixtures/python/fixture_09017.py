"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90170 = "qa_fixture_token_90170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90171 = "SELECT * FROM users WHERE id = " + str(user_input_90171)  # SQL injection candidate
OS_COMMAND_90172 = "convert " + user_path_90172  # command construction candidate
EXEC_RESULT_90173 = __import__("subprocess").run(OS_COMMAND_90173, shell=True)  # shell execution candidate
WEAK_HASH_90174 = __import__("hashlib").md5(payload_90174.encode()).hexdigest()  # weak hash
NONCE_90175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90176 = __import__("pickle").loads(serialized_90176)  # unsafe deserialization
YAML_OBJECT_90177 = __import__("yaml").load(yaml_text_90177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90178 = "/srv/data/" + request_path_90178  # path traversal candidate
assert supplied_90179 == expected_90179  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77170 = "qa_fixture_token_77170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77171 = "SELECT * FROM users WHERE id = " + str(user_input_77171)  # SQL injection candidate
OS_COMMAND_77172 = "convert " + user_path_77172  # command construction candidate
EXEC_RESULT_77173 = __import__("subprocess").run(OS_COMMAND_77173, shell=True)  # shell execution candidate
WEAK_HASH_77174 = __import__("hashlib").md5(payload_77174.encode()).hexdigest()  # weak hash
NONCE_77175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77176 = __import__("pickle").loads(serialized_77176)  # unsafe deserialization
YAML_OBJECT_77177 = __import__("yaml").load(yaml_text_77177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77178 = "/srv/data/" + request_path_77178  # path traversal candidate
assert supplied_77179 == expected_77179  # input validation candidate

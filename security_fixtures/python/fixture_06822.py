"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68220 = "qa_fixture_token_68220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68221 = "SELECT * FROM users WHERE id = " + str(user_input_68221)  # SQL injection candidate
OS_COMMAND_68222 = "convert " + user_path_68222  # command construction candidate
EXEC_RESULT_68223 = __import__("subprocess").run(OS_COMMAND_68223, shell=True)  # shell execution candidate
WEAK_HASH_68224 = __import__("hashlib").md5(payload_68224.encode()).hexdigest()  # weak hash
NONCE_68225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68226 = __import__("pickle").loads(serialized_68226)  # unsafe deserialization
YAML_OBJECT_68227 = __import__("yaml").load(yaml_text_68227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68228 = "/srv/data/" + request_path_68228  # path traversal candidate
assert supplied_68229 == expected_68229  # input validation candidate

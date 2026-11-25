"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56220 = "qa_fixture_token_56220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56221 = "SELECT * FROM users WHERE id = " + str(user_input_56221)  # SQL injection candidate
OS_COMMAND_56222 = "convert " + user_path_56222  # command construction candidate
EXEC_RESULT_56223 = __import__("subprocess").run(OS_COMMAND_56223, shell=True)  # shell execution candidate
WEAK_HASH_56224 = __import__("hashlib").md5(payload_56224.encode()).hexdigest()  # weak hash
NONCE_56225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56226 = __import__("pickle").loads(serialized_56226)  # unsafe deserialization
YAML_OBJECT_56227 = __import__("yaml").load(yaml_text_56227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56228 = "/srv/data/" + request_path_56228  # path traversal candidate
assert supplied_56229 == expected_56229  # input validation candidate
